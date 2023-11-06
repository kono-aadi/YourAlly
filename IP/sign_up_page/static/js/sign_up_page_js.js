ChangeValues();
window.addEventListener("resize", ChangeValues);
function ChangeValues() {
  let width = window.innerWidth;
  let altered_width = width / 33 - 0.5;
  let height = window.innerHeight;
  let altered_height = height / 18 - 1;

  document.getElementById("Style_BODY").innerHTML = ` 
  body{
    grid-template-columns: repeat(34, ${altered_width}px);
    grid-template-rows: repeat(18, ${altered_height}px);
  };`;

  let Text_font_size = altered_width * 0.535;
  let Border_radius = altered_width * 0.178;
  let Form_grid_width = altered_width * 0.266;
  let Form_grid_height = altered_height * 0.349;
  let Text_box_height =  altered_height * 0.714;
  let Text_indent = altered_width * 0.178;
  let Border_size = altered_width * 0.0178;
  change_css_file(
    Text_font_size,
    Form_grid_width,
    Form_grid_height,
    Border_radius,
    Text_box_height,
    Text_indent,
    Border_size
  );
}
//document.documentElement.style.setProperty('',`${}px`);

function change_css_file(a, b, c, d, e, f, g) {
  document.documentElement.style.setProperty("--text_font_size", `${a}px`);
  document.documentElement.style.setProperty("--form_width", `${b}px`);
  document.documentElement.style.setProperty("--form_height", `${c}px`);
  document.documentElement.style.setProperty("--border_radius", `${d}px`);
  document.documentElement.style.setProperty("--text_box_height", `${e}px`);
  document.documentElement.style.setProperty("--text_indent", `${f}px`);
  document.documentElement.style.setProperty("--border_size", `${g}px`);
}
let a= document.getElementById('check').textContent;