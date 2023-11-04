
ChangeValues();
window.addEventListener("resize", ChangeValues);

function ChangeValues() {
  let width          = window.innerWidth;
  let altered_width  = width / 33 - 0.5;
  let height         = window.innerHeight;
  let altered_height = height / 18 - 1;

  document.getElementById("Style_BODY").innerHTML = ` body{
    grid-template-columns: repeat(33, ${altered_width}px);
    grid-template-rows: repeat(18, ${altered_height}px);
  }   `;

  let Blur_bg_radius      = altered_width * 0.425;
  let Font_size           = altered_width * 0.552;
  let Name_font_size      = altered_width * 0.619;
  let Logo_width          = altered_width * 0.885;
  let Logo_height         = altered_width * 0.885;
  let Logo_margin         = altered_width * 0.265;
  let Input_width         = altered_width * 6.375;
  let Input_height        = altered_width * 0.708;
  let Log_in_font_size    = altered_width * 0.885;
  let Submit_width        = altered_width * 7.791;
  let Submit_height       = altered_width * 0.389;
  let Input_font_size     = altered_width * 0.283;
  let Submit_font_size    = altered_width * 0.389;

  change_css_file(
    Blur_bg_radius,
    Font_size,
    Name_font_size,
    Logo_width,
    Logo_height,
    Logo_margin,
    Input_width,
    Input_height,
    Log_in_font_size,
    Submit_width,
    Submit_height,
    Input_font_size,
    Submit_font_size
  );
}

// 2496

function change_css_file(a, b, c, d, e, f, h, i, j, k, l, m, n) {
  document.documentElement.style.setProperty("--blur_bg_radius"   , `${a}px`);
  document.documentElement.style.setProperty("--font_size"        , `${b}px`);
  document.documentElement.style.setProperty("--name_font_size"   , `${c}px`);
  document.documentElement.style.setProperty("--logo_width"       , `${d}px`);
  document.documentElement.style.setProperty("--logo_height"      , `${e}px`);
  document.documentElement.style.setProperty("--logo_margin"      , `${f}px`);
  document.documentElement.style.setProperty("--input_width"      , `${h}px`);
  document.documentElement.style.setProperty("--input_height"     , `${i}px`);
  document.documentElement.style.setProperty("--log_in_font_size" , `${j}px`);
  document.documentElement.style.setProperty("--submit_width"     , `${k}px`);
  document.documentElement.style.setProperty("--submit_height"    , `${l}px`);
  document.documentElement.style.setProperty("--input_font_size"  , `${m}px`);
  document.documentElement.style.setProperty("--submit_font_size" , `${n}px`);

}
