const url = 'http://127.0.0.1:5000/api/getGraph';

async function getData() {
    const response = await fetch(url)
    console.log(response);
}

getData();
