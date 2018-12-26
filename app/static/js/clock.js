var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var img = new Image();
ctx.drawImage(img, 100, 100);

/** 
var radius = canvas.height / 2;
ctx.translate(radius, radius);
radius = radius * 0.90
setInterval(drawClock, 1000);

function drawClock() {
  drawFace(ctx, radius);
  drawNumbers(ctx, radius);
  drawTime(ctx, radius);
}

function drawFace(ctx, radius) {
    var grad;

    ctx.beginPath();
    ctx.arc(0, 0, radius, 0, 2 * Math.PI);
    ctx.fillStyle = 'white';
    ctx.fill();
  

  
    ctx.beginPath();
    ctx.arc(0, 0, radius * 0.1, 0, 2 * Math.PI);
    ctx.fillStyle = '#333';
    ctx.fill();
}

function drawNumbers(ctx, radius) {
    var ang;
    var num;
    ctx.font = radius *0.15 +"px arial";
    ctx.textBaseline = "middle";
    ctx.textAlign = "center";
    for (num = 1; num < 13; num++) {
      ang = num * Math.PI / 6;
      ctx.rotate(ang);
      ctx.translate(0, -radius * 0.85);
      ctx.rotate(-ang);
      ctx.fillText(num.toString(), 0, 0);
      ctx.rotate(ang);
      ctx.translate(0, radius * 0.85);
      ctx.rotate(-ang); 

    }
}
function drawTime(ctx, radius) {
  var time = new Date();
  var hour = time.getHours();
  var minute = time.getMinutes();
  var second = time.getSeconds();
  hour = hour % 12;
  hour = ((Math.PI /6) * hour) + ((Math.PI/6) * minute / 60) + ((Math.PI / 6) * second / 360);
  drawHands(ctx, hour, radius * 0.5, radius *0.07);
  minute = ((Math.PI/30) * minute) + ((Math.PI/30) * second / 60);
  drawHands(ctx, minute, radius * 0.7, radius * 0.05);
  second = ((Math.PI/30) * second);
  drawHands(ctx, second, radius * 0.8, radius * 0.03);
}
function drawHands(ctx, pos, length, width) {
  ctx.beginPath();
  ctx.lineWidth = width;
  ctx.lineCap = "round";
  ctx.moveTo(0,0);
  ctx.rotate(pos);
  ctx.lineTo(0, -length);
  ctx.stroke();
  ctx.rotate(-pos);
}
**/
