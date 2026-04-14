async  function calcular(){

    const valor = document.getElementById("valor").value;
    const nome = document.getElementById("nome_cliente").value;
    const desconto = document.getElementById("desconto").value;
    const tipo_cliente = document.getElementById("tipo_cliente").value;

    const vip = tipo_cliente === "vip";

    const response = await fetch("/api/calcular", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({valor, desconto, vip, nome})
    });

    const data = await response.json();

    if (data.erro) {alert("Erro: " + data.erro);
    return;
    }

    document.getElementById("resultado").textContent = `O valor do cashback: R$ ${data.cashback.toFixed(2)}`;
}

async function CarregarHistorico(){

    const response = await fetch("/api/historico");
    const historico = await response.json();    

    const historicoList = document.getElementById("historico-list");
    historicoList.innerHTML = "";

    historico.forEach(item => {
        const listItem = document.createElement("li");
        listItem.textContent = `Valor: R$ ${item.valor}, Desconto: ${item.desconto}%, Cashback: R$ ${item.cashback.toFixed(2)}`;
        historicoList.appendChild(listItem);
    });
}

function botao_Historico() {
    const container = document.getElementById("historico-container");

    if (container.style.display === "none") {
        container.style.display = "block";
        CarregarHistorico();
    } else {
        container.style.display = "none";
    }
}

