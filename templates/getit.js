function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;

  const deleteButton = card.querySelector(".delete-btn");
  deleteButton.addEventListener("click", function () {
    card.remove();
    // Chame a função para deletar no servidor (você precisará implementar isso)
  });

  const editButtons = document.querySelectorAll(".edit-btn");
  editButtons.forEach((editButton) => {
  editButton.addEventListener("click", function () {
    const noteId = this.getAttribute("data-id");
    // Lógica para abrir um formulário de edição e preencher os campos
    });
  });

  const criarBtn = document.getElementById("criarBtn");

  criarBtn.addEventListener("click", function () {
  const tituloInput = document.getElementById("titulo");
  const detalhesInput = document.getElementById("detalhes");

  const titulo = tituloInput.value;
  const detalhes = detalhesInput.value;

  if (titulo && detalhes) {
    // Chame a função para enviar a nova nota para o servidor
    criarNotaNoServidor(titulo, detalhes);

    // Crie um novo card na interface
    criarNovoCard(titulo, detalhes);

    // Limpe os campos de entrada
    tituloInput.value = "";
    detalhesInput.value = "";
  }
});

function criarNotaNoServidor(titulo, detalhes) {
  // Faça uma solicitação POST ao servidor para criar a nova nota
  // Implemente isso de acordo com sua estrutura de servidor
}

function criarNovoCard(titulo, detalhes) {
  const cardContainer = document.querySelector(".card-container");

  const newCard = document.createElement("div");
  newCard.className = "card card-color-1 card-rotation-1"; // Modifique conforme necessário
  newCard.innerHTML = `
    <h3 class="card-title">${titulo}</h3>
    <div class="card-content">
      <button class="delete-btn">Excluir</button>
      <button class="edit-btn">Editar</button>
      <p>${detalhes}</p>
    </div>
  `;

  cardContainer.appendChild(newCard);

  // Adicione manipuladores de eventos aos botões "Excluir" e "Editar" aqui
  const deleteButton = newCard.querySelector(".delete-btn");
  deleteButton.addEventListener("click", function () {
    // Lógica para excluir a nota (enviar solicitação para o servidor)
  });

  const editButton = newCard.querySelector(".edit-btn");
  editButton.addEventListener("click", function () {
    // Lógica para editar a nota (preencher formulário de edição)
  });
}


  }
});
