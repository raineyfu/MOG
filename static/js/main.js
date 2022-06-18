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