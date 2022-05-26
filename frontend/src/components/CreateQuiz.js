
import React, {Fragment} from 'react';
import axios from 'axios';


class CreateQuiz extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            questions: [],
            name: "",
            selectedQuestions: []
        }
    }
    
    componentDidMount() {
        let response =   axios.get('/questions/').then(({data}) => {
            debugger
            this.setState({
                questions: data,
                selectedQuestions: new Array(data.length + 1).fill(false)
            })
          })
          .catch(err => console.log(err))
    }

    handleNameChange = event => {
        event.preventDefault();
        this.setState({name: event.target.value})
    }

    handleOnChange = position => {
        const { selectedQuestions } = this.state
        const updatedSelectedQuestions = selectedQuestions.map((item, index) => 
            index === position ? !item : item
        )
        this.setState({
            selectedQuestions: updatedSelectedQuestions
        })
    }

    handleOnSubmit = event => {
        event.preventDefault()
        const { name, selectedQuestions } = this.state
        const selected = selectedQuestions.flatMap((bool, index) => bool ? index : [])
        if(name && selected.length > 0) {
            debugger;
            let data = {
                name,
                questions: selected.toString(),
                csrf_token: document.cookie.split('; csrftoken=')[1]
            }
            axios.post('create-quiz/', data)
            .then(res => alert(res.data));
        }
        else{
            alert('both name and questions should be avaible to create a quiz');
        }
    }

    render() {
        const { name, questions, selectedQuestions } = this.state
        return (
            <form onSubmit={this.handleOnSubmit}>
                <input type="submit" value="Create Quiz" /><br/>
                <input type="text" name="name" placeholder="name" onChange={this.handleNameChange} value={name} />
                <h1>All Questions (Select them to make a quiz)</h1>
                {questions ? (
                    questions.map((question, index) => (
                        <div>
                            <hr />
                            <input
                                type="checkbox"
                                name="selected_questions"
                                value={question.id}
                                checked={selectedQuestions[question.id]}
                                onChange={() => this.handleOnChange(question.id)}
                            />
                            <p>{question.category}</p>
                            <p>{question.text}</p>
                            <p>{question.type}</p>
                            <p>{question.difficulty}</p>
                            <p>{question.correct_answer}</p>
                            <p>{question.incorrect_answer}</p>
                        </div>
                    ))
                ) : (
                    <p>No question found!</p>
                )}
            </form>
        )
    }
}

export default CreateQuiz