import React from 'react';
import axios from 'axios';

class App extends React.Component {
 state = {
   Post: []
 }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/post')
      .then(res => {
        const Post = res.data;
        this.setState({ Post });
      })
  }

  render() {
    return (
      <ul>
        {
          this.state.Post
            .map(Post =>
              <div key={Post.id}>
              <h1>{Post.title}</h1>
                <h2>{Post.author}</h2>
                <h3>{Post.created_at}</h3>
                <p>{Post.body}</p>
              </div>
            )
        }
      </ul>
    )
  }
}

export default App;