import requests


def Get(url, PostId):
	try:
		isinstance(int(PostId), int)
		if int(PostId) <= 100 and int(PostId) > 0:
			r = requests.get(url + PostId)
			return r
		else:
			print("Number must be between 1 and 100")
	except ValueError as err:
		raise(err)
	return "No Results"

def Post(PostUrl,title, body, userId=11):
	Post= {
		'title': title,
		'body': body,
		'userId': userId
		}
	request = requests.post(PostUrl, data=Postdata)
	return request

def main():
	print("Python HTTP API command line app %s\n" %("-"*31))
	print("Simple Python HTTP API command line app")
	
	url = "https://jsonplaceholder.typicode.com/posts/"

	PostId = input("Enter a number between 1 and 100: ")
	get = Get(url,PostId)
	print("GET Response data\n\t%s\n%s\n\tStatus code\n\t%s\n%s\n\tHeaders\n\t%s\n%s" % 
		("-"*17,get.text, "-"*11, get.status_code,"-"*7, get.headers))

	title = input("Enter a title for your post: ")
	body = input("Enter a body for your post: ")

	post = Post(url,title,body)
	print("\tPOST Response data\n\t%s\n%s\n\tStatus code\n\t%s\n%s\n\tHeaders\n\t%s\n%s" % 
		("-"*17,post.text, "-"*11, post.status_code,"-"*7, post.headers))

if __name__ == '__main__':
     main()
