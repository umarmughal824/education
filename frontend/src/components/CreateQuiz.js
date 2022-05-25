
import React, {Fragment} from 'react';
import axios from 'axios';


class CreateQuiz extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            questions: [],
        }
    }
    
    componentDidMount() {
        let response =   axios.get('/questions/').then(({data}) => {
            debugger
            this.setState({questions: data})
          })
          .catch(err => console.log(err))
    }

    render() {
        const { questions } = this.state
        return (
            <Fragment>
                <h1>All Questions (Select them to make a quiz)</h1>
                {questions ? (
                    questions.map(question => (
                        <div>
                            <hr />
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
            </Fragment>
        )
    }
}

export default CreateQuiz