import React from 'react';
import axios from 'axios';

class App extends React.Component {
 state = {
   Post: []
 }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/post', 'http://127.0.0.1:8000/api/users' )
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
                <p>{Post.body}</p>
                <img alt='Img' src={Post.image}/>
                  <div>
                    <div>{Post.author}</div>
                    <p3>{Post.created_at}</p3>
                  </div>
              </div>
            )
        }
      </ul>
    )
  }
}

export default App;