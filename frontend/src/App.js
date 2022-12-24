import React from 'react';
import axios from 'axios';
import './App.css';

class App extends React.Component {
 state = {
   Post: []
 }

  componentDidMount() {
    axios.get('http://localhost:8000/api/post')
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
              <h1 className='title' >{Post.title}</h1>
                <p className='body'>{Post.body}</p>
                  <img className='image' alt='Img' src={Post.image}/>
                  <div>
                    <div className='author'>{Post.author}</div>
                    <p3 className='created_at'>{Post.created_at}</p3>
                  </div>
              </div>
            )
        }
      </ul>
    )
  }
}

export default App;