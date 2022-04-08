import json
from flask import Flask, request,Response
#from flask_pymongo import PyMongo
from bson import json_util
from flask_mongoengine import MongoEngine
from mongoengine import ReferenceField, ListField
from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId
#--------------------------------------------------------------------------------------
app= Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/'
client = MongoClient()
#name of the database on mongodb
mydb = client["practicas"]
#mongo=PyMongo(app)
dbs = MongoEngine()
#name of the colection inside of the database("practicas") on mongodb
mycol = mydb["taxons"]
#colection files to save the file to download or update
myfiles = mydb["fs.files"]

#--------------------------------------------------------------------------------------
class File(dbs.Document):
    name=dbs.StringField()
    type=dbs.StringField()
    file=dbs.BinaryField()  


class Taxon(dbs.Document):
    taxid = dbs.StringField()
    name = dbs.StringField()
    #files=ListField(ReferenceField(File))
    files= ListField(ReferenceField('File'))

#--------------------------------------------------------------------------------------

@app.route('/taxons', methods=['GET'])
def find_all_taxons():
    """This function will be display the list of all the taxons in the db"""

    taxons=mycol.find()
    response=json_util.dumps(taxons)
    return Response(response,mimetype="application/json") 

#--------------------------------------------------------------------------------------

@app.route('/taxons/<taxid>', methods=['GET'])
def find_taxon_by(taxid):
    """This function will be display only one taxons by taxid"""

    taxons=mycol.find_one({"taxid":taxid})
    response=json_util.dumps(taxons)
    if response == "null":
        info={
                "taxid":"","name":"","file":[{
                    "name": "",
                    "type": "",
                    "file": ""
                }]}
        response=json_util.dumps(info)
        return Response(response,mimetype="application/json") 

    return Response(response,mimetype="application/json") 



#--------------------------------------------------------------------------------------
@app.route('/upload', methods=['PUT'])
def upload_file():
    """This function its for upload info on the db for do the tests"""


    file_location="/home/edu/Desktop/sequence.fasta" 
    name="sequence.fasta"
    sep = '.'
    name_file = name.split(sep, 1)[0]
    type_file = name.split(sep, 1)[1]

    taxon = json.loads(request.data)

    file_data=open(file_location,"rb")
    data=file_data.read()
    fs=gridfs.GridFS(mydb)
    file_name=fs.put(data,filename=name)

    mycol.insert_many(
             [{"taxid":taxon['taxid'],"name":taxon['name'],"file":[{
                 "name": name_file,
                 "type": type_file,
                 "file": file_name
             }]}]
         )
    info={
              "taxid":taxon['taxid'],"name":taxon['name'],"file":[{
                 "name": name_file,
                 "type": type_file,
                 "file": file_name
             }]}
    response=json_util.dumps(info)
    return  response

#--------------------------------------------------------------------------------------
@app.route("/files/<id>")
def download_file(id):
    """This function will be download the file by file name"""

    data=myfiles.find_one({"filename":id})
    print(data)
    if data ==None:
        return "No se encontro ninguno"
    else:
        my_id=data["_id"]
        fs=gridfs.GridFS(mydb)
        outputdata=fs.get(my_id).read()
        download_location="/home/edu/Desktop/descargas_mongodb/" +id
        output=open(download_location,"wb")
        output.write(outputdata)
        output.close()
        return "Download succesful!"


#--------------------------------------------------------------------------------------
@app.route("/delete",methods=["DELETE"])
def delete_all():
    """This function will be delete all info of the db"""

    x = mycol.delete_many({})

    return "deleted"



if __name__ == "__main__":
    app.run(debug=True)
