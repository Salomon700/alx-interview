#!/usr/bin/node
const request = require("request");
const API_URL = "https://swapi-api.hbtn.io/api";

if (process.argv.length === 3) {
    request(`${API_URL}/films/${process.argv[2]}`, (err, _, body) => {
        if (err) {
            console.error(err);
            return;
        }
        const charactersURL = JSON.parse(body).characters;
        const charactersName = charactersURL.map(
            (url) => new Promise((resolve, reject) => {
                request(url, (err, _, body) => {
                    if (err) {
                        reject(err);
                    }
                    resolve(JSON.parse(body).name);
                });
            })
        );

        Promise.all(charactersName)
            .then(names => console.log(names.join("\n")))
            .catch(err => console.log(err));
    });
}
