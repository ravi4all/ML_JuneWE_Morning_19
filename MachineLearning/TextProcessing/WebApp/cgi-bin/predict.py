# python -m http.server --cgi 9797

import cgi
import sentimentAnalysis

form = cgi.FieldStorage()
review = form.getvalue("review")

pred = sentimentAnalysis.testPrediction(review)

if pred[0] == 0:
    msg = "Negative"
else:
    msg = "Positive"

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>Prediction Analysis</h1>
    <h2>Prediction is {}</h2>
</body>
</html>""".format(msg))
