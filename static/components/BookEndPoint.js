const e = React.createElement;

class ClickCounter extends React.Component {
    // Constructor 
    constructor(props) {
        super(props);

        this.state = {
            items: [],
        };
    }


    fetchAPI() {

        var url = `http://127.0.0.1:8000/api/books`;


        fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token 6cfb8759283d450e67eab050777abcb8f52768c8',
            }
        }).then(response => {
            if (response.ok) {
                return response.json();
            }
        }).then(data => {
            console.log(data)

        }).catch((error) => {
            console.error('Error:', error);
        });

    }

    render() {
        return e(
            'button',
            {
                onClick: () => { this.fetchAPI() },

            },
            'Click'
        );
    }
}

ReactDOM.render(e(ClickCounter), document.getElementById('react_container'))



