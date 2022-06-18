var taskListOpen = false;


document.getElementById("taskList").addEventListener("click", function(event) {
    taskListOpen = !taskListOpen;
    var taskList = document.getElementById("taskList");

    if (taskListOpen) {
        for (var counter = 0; counter < taskList.children.length; counter++) {
            var child = taskList.children[counter];
            child.style.display = "block";
        }
    } else {
        for (var counter = 0; counter < taskList.children.length; counter++) {
            var child = taskList.children[counter];
            child.style.display = "none";
        }
    }
});