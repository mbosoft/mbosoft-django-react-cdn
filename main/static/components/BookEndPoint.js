const e = React.createElement;

class BookEndPoint extends React.Component {
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
                'Authorization': 'Token faf2e29353eba5ff3df2fcfeba3cf9afb3b096b2',
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

ReactDOM.render(e(BookEndPoint), document.getElementById('react_container'))



