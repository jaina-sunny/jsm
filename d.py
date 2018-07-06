from flask import Flask
from flask import request 

app = Flask(__name__)


@app.route('/about',methods=['GET'])
def hai_world():
	value = request.args.get('name')
        value1 = request.args.get('age')
	return value+value1;
	




if __name__ == "__main__":
        print "hello world"
	app.run()

