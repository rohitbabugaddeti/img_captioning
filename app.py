from flask import Flask, request, render_template, flash, redirect, url_for
import os
import requests

app = Flask(__name__)
UPLOAD_FOLDER ="uploaded image"
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        file = request.files['fileupload']
        file_name = file.filename
        url = request.form['url']
        # print(file_name == '' and url == '')
        if file_name and url:
            return render_template('error.html',
                                   action = "given",
                                   error = "multiple inputs",
                                   to_do = "give",
                                   ac_type = "single input",
                                   accepted_content = "valid single input is")
        elif file_name == '' and url == '':
            flash('No file/url given')
            return redirect(url_for('index'))
        else:
            if url:
                try:
                    resp = requests.get(url)
                    file_type = resp.headers["Content-Type"]
                    if resp.status_code == 200 and "image" in resp.headers["Content-Type"].lower():
                        with open(os.path.join(app.config['UPLOAD_FOLDER'], "uploaded_img."+ file_type[file_type.rfind("/")+1:]), 'wb') as imf:
                            imf.write(resp.content)
                    else:
                        return render_template("error.html",
                                               action = "given",
                                               error = "Invalid URL",
                                               ac_type = "URL",
                                               to_do = "give",
                                               accepted_content = "valid image URLs are")
                except Exception as e:
                    return render_template("error.html",
                                           action = "given",
                                           error = "Invalid URL",
                                           ac_type = "URL",
                                           to_do = "give",
                                           accepted_content = "image URL is")
            else:
                if allowed_file(file_name):
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_img' + file_name[file_name.rfind("."):]))
                else:
                    return render_template('error.html',
                                           action = "uploaded",
                                           error = "Invalid File",
                                           ac_type="image file",
                                           to_do = "upload",
                                           accepted_content = "JPG/JPEG, PNG files are")

    return url

@app.route("/error")
def error():
    return render_template('error.html')

if __name__ == "__main__":
    app.secret_key = "img_bot"
    app.run(debug=True)
