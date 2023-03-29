document.addEventListener("DOMContentLoaded", () => {
    // const key = "9e3f7ce4-b9a7-4244-b709-dae5c1f1d4a8";
    

    

    document.getElementById("find-btn").onclick = function() {
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