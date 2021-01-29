from datetime import datetime
from flask import Flask, jsonify, request,render_template
from flask_dropzone import Dropzone
from elasticsearch import Elasticsearch
#from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
import importlib
import numpy as np
import glob
import matplotlib.pyplot as plt
import cv2
import upload_image as up
#import similar
#moduleName = input('similar.py')
#importlib.import_module(moduleName)
#from similar import similar

app = Flask(__name__)
es = Elasticsearch()
dropzone = Dropzone(app)

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = False
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
file_name =None
# Uploads settings
#app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

#photos = UploadSet('photos', IMAGES)
#configure_uploads(app, photos)
#patch_request_class(app)

@app.route('/results')
def results():
	print(file_name)
	up.search_by_style(file_name)
	image_names1= []
	image_names1 = os.listdir('C:/Users/rishv/OneDrive/Northeastern/SEM3/Algorithmic Digital Marketing/Assignments/Assignment3/Flask/static/displayimage')
	return render_template('results.html',image_name=image_names1)


@app.route('/',methods=["POST","GET"])
def index():
	if request.method == 'POST':
		file_obj=request.files['file']
		global file_name
		file_name=file_obj.filename
		return "uploading..."

	return render_template('index.html')

@app.route('/similarimages',methods=["POST","GET"])	
def  similarimages():		
	q=request.args.get("q")
	#q=request.form.get("q")
	if q is not None:
		resp=es.search(index='series',doc_type='series',body={ "_source": ["similar_pi"],"query": { "query_string": { "query":q, "fields": ["master_pi"] } } })
		similar_pi =[]
		#print(resp)
		for i in resp['hits']['hits']:
			similar_pi.append(i['_source']['similar_pi'])
		#print("similar_pi",similar_pi)
		def similar(similar_pi):
			#print("into similar.py")
			path = 'C:/Users/rishv/OneDrive/Northeastern/SEM3/Algorithmic Digital Marketing/Assignments/Assignment3/Flask/static/similar_image'
			image_paths = glob.glob('C:/Users/rishv/OneDrive/Northeastern/SEM3/Algorithmic Digital Marketing/Assignments/Assignment3/Dataset/image/*.jpg')
			del_paths = glob.glob('C:/Users/rishv/OneDrive/Northeastern/SEM3/Algorithmic Digital Marketing/Assignments/Assignment3/Flask/static/similar_image/*.jpg')
			for i in del_paths:
				os.remove(i)
			for i in similar_pi:
				#print(i)
				for filename in image_paths: 
					image = cv2.imread(filename, 3)
					b,g,r = cv2.split(image) # get b, g, r
					image = cv2.merge([r,g,b]) # switch it to r, g, b
					#image = cv2.resize(image, (200, 200))
					x = os.path.basename(filename)
					y = str(i)+'_0.jpg'
					#picture = imread(io.BytesIO(pic['picture']))
					if(y==x):
						picture_file = os.path.join(path, x)
						#print(picture_file)
						plt.imsave(picture_file, image)
						print("saved")
		similar(similar_pi)
		image_names = os.listdir('C:/Users/rishv/OneDrive/Northeastern/SEM3/Algorithmic Digital Marketing/Assignments/Assignment3/Flask/static/similar_image')
		return render_template('images.html',q=q,image_name=image_names)

	return render_template('images.html')

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__=="__main__":
	app.run(debug=True,port=8000)
