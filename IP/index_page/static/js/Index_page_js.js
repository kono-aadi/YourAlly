
ChangeValues();
window.addEventListener("resize", ChangeValues);
function ChangeValues() {
  let width = window.innerWidth;
  let altered_width = width / 33 - 0.5;
  let height = window.innerHeight;
  let altered_height = height / 18 - 1;

  document.getElementById("Style_BODY").innerHTML = ` body{
    grid-template-columns: repeat(34, ${altered_width}px);
    grid-template-rows: repeat(18, ${altered_height}px);
  }   `;

  let logo_width=altered_width*4.491;
  let logo_height=altered_height*4.491;
  let Name_font_size=altered_width*1.147;
  let Text_font_szie=altered_width*0.524590;
  let Border_radius_blurbg=altered_width*0.8196;
  let Button_width=altered_width*1.5737;
  let Button_height=altered_height*0.6885245;
  let Button_font_size=altered_width*0.3606557;
  let Border_radius_button=altered_width*0.196721311;
  let Line_spacing=altered_width*0.0892;

  change_css_file(logo_width,logo_height,Name_font_size,Text_font_szie,Border_radius_blurbg,Button_width,Button_height,Button_font_size,Border_radius_button,Line_spacing);
}

//1.573770

function change_css_file(x,y,z,u,v,q,e,i,j,k){
    document.documentElement.style.setProperty("--logo_width",`${x}px`);
    document.documentElement.style.setProperty("--logo_height",`${y}px`);
    document.documentElement.style.setProperty("--name_font_size",`${z}px`);
    document.documentElement.style.setProperty("--text_font_size",`${u}px`);
    document.documentElement.style.setProperty("--border_radius_blurbg",`${v}px`);
    document.documentElement.style.setProperty("--button_width",`${q}px`);
    document.documentElement.style.setProperty("--button_height",`${e}px`);
    document.documentElement.style.setProperty("--button_font_size",`${i}px`);
    document.documentElement.style.setProperty("--border_radius_button",`${j}px`);
    document.documentElement.style.setProperty("--line_spacing",`${k}px`);
}
