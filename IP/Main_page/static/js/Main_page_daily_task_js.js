
function add() {
    let count = 0;
    
    let Task = "task";
    let Dat = "date";
    let Time = "time";
    let Desc = `description`;
    let streak=0;
    for (let i = 0; i < 15; i += 1) {
      document.getElementById("box").innerHTML += `
              <div class="main">
              <form method='POST' class="card">
                  <div class="task_name">Task: ${Task}</div>
                  <div class="content">Description:<br> ${Desc}</div>
                  <div class="streaks">streak: ${streak}</div>
                  <div class="delete"><img src="/static/images/Bin.png" alt="del"></div>
                  <div class='streak_count'> <button>Done</button></div>
                  <div class="completed"><img src="/static/images/Check.png" alt="check"></div>
              </form>
              </div>
              
              
              `;
      count += 1;
    }
  }
  add();