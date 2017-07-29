setInterval(function(){
  $.get('/price',function(data) {
      document.title = `($${data.price}) NEO Price`;
      document.getElementById("p1").innerHTML = `1 NEO - $${data.price}`;
      document.getElementById("p2").innerHTML = `$${data.high}`;
      document.getElementById("p3").innerHTML = `$${data.low}`;
      if (data.decrease) {
        document.getElementById("p4").className = "decrease";
        document.getElementById("p4").innerHTML = `$${data.change}<i class="triangle-down">`;
      } else {
        document.getElementById("p4").className = "increase";
        document.getElementById("p4").innerHTML = `$${data.change}<i class="triangle-up">`;
      }
  });
}, 30000);
