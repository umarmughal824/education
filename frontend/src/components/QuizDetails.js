import React, { Fragment } from 'react'
// import { withRouter } from "react-router";
import axios from 'axios';
import { useParams } from "react-router-dom";

function withParams(Component) {
  return props => <Component {...props} params={useParams()} />;
}

  
class QuizDetails extends React.Component {
  // params = useParams();
  constructor(props) {
    // let { id } = useParams();
    super(props);
    this.state = {
      quiz: [],
      // id
    }
  }

  componentDidMount() {
    const {id} = this.props.params
    

    axios
    .get(`/allquizes/${id}/`).then(({data}) => {
      this.setState({quiz: data})
    })
    .catch(err => console.log(err))
  }

  render() {
    const {quiz} = this.state
    return (
      <Fragment>
        <h1>Quize</h1>
        <span>{quiz.name}</span>
        <h1>All Question</h1>
                {quiz.questions ? (
                    quiz.questions.map((question, index) => (
                        <div>
                            <hr />
                            {/* <input
                                type="checkbox"
                                name="selected_questions"
                                value={question.id}
                                checked={selectedQuestions[question.id]}
                                onChange={() => this.handleOnChange(question.id)}
                            /> */}
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

export default withParams(QuizDetails)

