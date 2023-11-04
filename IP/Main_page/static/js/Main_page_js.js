
function add() {
  let List_of_Tasks1 = JSON.parse(document.getElementById("List_of_Tasks_main").textContent);

  let no;
  no = List_of_Tasks1.length;

  let count = 0;

  let Task;
  let Dat = "date";
  let Time = "time";
  let Desc;
  let ID;
  if (List_of_Tasks1 == []) {
  } else {
    for (let i = 0; i < no; i += 1) {
      Task = List_of_Tasks1[i][0];
      Desc = List_of_Tasks1[i][1];
      ID   = List_of_Tasks1[i][3]
      document.getElementById("box").innerHTML += `
                <div class="main">
                <div class="card" class='${ID}'>

                    <div class="task_name">Task: ${Task}</div>
                    <div class="date">id: ${Dat}</div>
                    <div class="time">Time: ${Time}</div>
                    <div class="content">Description:<br> ${Desc}</div>
                    <a href= "{% url 'delete-task' ${ID} %} " class="delete"> <div ><button>Delete</button></div></a>
                    <div class="completed"><button>Done</button></div>
                </div>
                </div>
                
                `;
      count += 1;
    }
  }
}



function add_task() {
  document.getElementById("pop_up").style.display = "block";
  document.getElementById("box").style.display = "none";
}

function close_task() {
  document.getElementById("pop_up").style.display = "none";
  document.getElementById("box").style.display = "flex";
}
function Submit() {
  document.getElementById("pop_up").style.display = "none";
  document.getElementById("box").style.display = "flex";
}

close_task();

