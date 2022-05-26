import React, { Fragment } from 'react'
import axios from 'axios';


  
class Quizes extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      quizes: [],
    }
  }

  componentDidMount() {
    axios
    .get(`/allquizes/`).then(({data}) => {
      this.setState({quizes: data})
    })
    .catch(err => console.log(err))
  }

  render() {
    const {quizes} = this.state
    return (
      <Fragment>
        <h1>Quizes</h1>
        {quizes.map(quiz => (
          // const link = 
          <div>
            <hr />
            <a href={`/quizes/${quiz.id}`}>{quiz.id}. {quiz.name}</a>
          </div>
        ))}
      </Fragment>
    )
  }
}

export default Quizes
