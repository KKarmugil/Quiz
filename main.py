from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return """
        
        <style>
body {
    background-color: #333;
    color: #fff;
    font-family: 'Montserrat', sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

form {
    background-color: #444;
    padding: 50px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px #000;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 600px;
}

label {
    font-size: 20px;
    margin-bottom: 20px;
}

input[type="text"], input[type="submit"] {
    padding: 10px 20px;
    font-size: 16px;
    width: 100%;
    margin-bottom: 20px;
    box-sizing: border-box;
    border-radius: 5px;
    border: none;
}

input[type="text"] {
    background-color: #fff;
    color: #333;
}

input[type="submit"] {
    background-color: #ff3300;
    color: #fff;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
}

input[type="submit"]:hover {
    transform: scale(1.1);
}

a {
    color: #ff3300;
    text-decoration: none;
    margin-top: 20px;
}

.back-button {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border-radius: 5px;
    border: 2px solid #ff3300;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: center;
    margin-top: 20px;
}

.back-button:hover {
    background-color: #ff3300;
    color: #333;
}

.success {
    background-color: #333;
    color: #fff;
    padding: 50px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px #000;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 600px;
    text-align: center;
}

.success h1 {
    font-size: 32px;
    margin-bottom: 20px;
}
</style>


        <form action="add_data" method="post">
            <label for="question">Question:</label>
            <input type="text" id="question" name="question"><br><br>
            <label for="options">Options:</label>
            <input type="text" id="options" name="options"><br><br>
            <label for="answer">Answer:</label>
            <input type="text" id="answer" name="answer"><br><br>
            <input type="submit" value="Submit">
        </form>
    """

@app.route("/add_data", methods=["POST"])
def add_data():
    question = request.form["question"]
    options = request.form["options"].split(",")
    answer = request.form["answer"]
    
    data = {
        "question": question,
        "options": options,
        "answer": answer
    }
    
    try:
        with open("data.json", "r") as f:
            existing_data = json.load(f)
    except:
        existing_data = []
    
    existing_data.append(data)
    
    with open("data.json", "w") as f:
        json.dump(existing_data, f)
    
    return "Data added successfully<br><a href='/'>Go Back</a>"


if __name__ == "__main__":
    app.run()
