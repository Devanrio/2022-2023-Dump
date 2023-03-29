document.addEventListener("DOMContentLoaded", () => {
    // const key = "68d6cb634e90ac32c4bb80689aa7fbc3";

    document.getElementById("submit-btn").onclick = function() {
        const request = new XMLHttpRequest();
        request.onload = function() {
            const data = JSON.parse(this.responseText);
            // let ulElement = document.createElement("ul");
            
            Object.keys(data.rates).forEach(key => {
                const tr = document.createElement("tr");
                const currency = document.createElement("td");
                const rates = document.createElement("td");
                currency.innerHTML = key;
                rates.innerHTML = data.rates[key];
                // listItem.innerHTML = `${key} : ${data.rates[key]}`;
                // ulElement.append(listItem);
                tr.append(currency);
                tr.append(rates);
                document.querySelector(".res-table").append(tr);
            });
            
        }
        request.open("GET", `http://127.0.0.1:5000/api/currency/latest`);
        request.send();

        return false;
    }
})