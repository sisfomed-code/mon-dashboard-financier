from flask import Flask, request, jsonify, render_template_string
from agent import ask_agent

app = Flask(__name__)


PAGE = """
<!DOCTYPE html>
<html lang="fr">

<head>

<meta charset="UTF-8">

<title>KLConsulting AI</title>

<style>

body {
    font-family: Arial;
    background:#f2f5f3;
    max-width:900px;
    margin:40px auto;
    padding:20px;
}

.container {
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0 0 15px #ccc;
}

h1 {
    color:#166534;
}

#question {
    width:80%;
    padding:12px;
    font-size:16px;
}

button {
    padding:12px 20px;
    background:#166534;
    color:white;
    border:none;
    border-radius:5px;
    cursor:pointer;
}

#reponse {
    margin-top:25px;
    padding:20px;
    background:#f0fdf4;
    border-radius:10px;
    white-space:pre-wrap;
}

</style>

</head>


<body>

<div class="container">

<h1>🤖 KLConsulting AI</h1>

<p>
Votre assistant intelligent de formation informatique.
</p>


<input id="question"
placeholder="Posez votre question..."
>


<button onclick="envoyer()">
Envoyer
</button>


<div id="reponse">
La réponse apparaîtra ici...
</div>


</div>


<script>

function envoyer(){

let question =
document.getElementById("question").value;


document.getElementById("reponse").innerHTML =
"⏳ Analyse en cours...";


fetch("/chat", {

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
question:question
})

})


.then(response=>response.json())

.then(data=>{

document.getElementById("reponse").innerHTML =
data.reponse;

})


.catch(error=>{

document.getElementById("reponse").innerHTML =
"Erreur : "+error;

});

}

</script>


</body>

</html>
"""


@app.route("/")
def accueil():

    return render_template_string(PAGE)



@app.route("/chat", methods=["POST"])
def chat():

    data=request.json

    question=data.get("question")


    reponse=ask_agent(question)


    return jsonify({

        "reponse":reponse

    })



if __name__=="__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )