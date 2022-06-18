var app = new Framework7({
  root: '#app',
  name: 'My App',
  id: 'com.myapp.test',
  routes: [
    // Add your routes here
    // Example:
    /*
    {
      path: '/about/',
      url: 'about.html',
    },
    */
  ],
});

var mainView = app.views.create('.view-main');

var calendar = app.calendar.create({
  containerEl: '#open-calendar',
  on: {
    change: (cal, val) => {
      console.log(val); 
    }
  }
});

var list = document.getElementsByClassName("calendar-day");
for (var counter = 0; counter < list.length; counter++) {
  list[counter].addEventListener("click", function() {;
    let text;
    let redirect = prompt("Which journal entry would you like to view?", "Entry 1");
    
    switch(redirect) {
      case "Entry 1":
        window.location.replace("journal.html");
        document.getElementById("demo2").innerHTML = result;
        break;
      case "Entry 2":
        window.location.replace("journal.html");
        document.getElementById("demo2").innerHTML = result;
        break;
      case "Entry 3":
        window.location.replace("journal.html");
        document.getElementById("demo2").innerHTML = result;
        break;
      default:
        text = "No journal entry found!";
    }  
  });
}
