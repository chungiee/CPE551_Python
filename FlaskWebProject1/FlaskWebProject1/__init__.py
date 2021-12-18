"""
The flask application package.
"""

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
import FlaskWebProject1.views

app.config["UPLOAD_PATH"] = "D:/School/Seventh Semester/Python/PhotoDrive/FlaskWebProject1/FlaskWebProject1/static/Uploads"

# Route for handling document upload to static/Uploads folder
@app.route("/documents", methods=["GET","POST"])
def upload_docs():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):    #request the name of the file you want to upload
            f=request.files['file_name']
            f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))  #saves file into directory
        return render_template("documents.html", msg="Files have been uploaded successfully")
    return render_template("documents.html", msg="Please choose a file")

# Route for handling photo upload to path folder static/Uploads
@app.route("/photos", methods=["GET","POST"])
def upload_photos():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
            f=request.files['file_name']
            f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
        return render_template("photos.html", msg="Files have been uploaded")
    return render_template("photos.html", msg="Choose a file")
  
# For future improvements: tackle on displaying docs/photos uploaded to server
    #@app.route("/uploads")
    #def upload_list():
    #    imageList = os.listdir(UPLOAD_PATH)
    #    imageList = ['Uploads/' + image for image in imageList]
    #    return render_template("uploads.html", imageList=imageList)

if __name__ == '__main__':
    app.run(debug=True)

