<!DOCTYPE html>
<html>
<head>
    <title>LMS App</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>LMS App</h1>
        <div class="row">
            <div class="col-md-6">
                <h2>Create Course</h2>
                <form id="create-course-form">
                    <div class="mb-3">
                        <label for="course-title" class="form-label">Course Title:</label>
                        <input type="text" class="form-control" id="course-title" required>
                    </div>
                    <div class="mb-3">
                        <label for="course-description" class="form-label">Course Description:</label>
                        <textarea class="form-control" id="course-description" rows="10" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Create Course</button>
                </form>
            </div>
            <div class="col-md-6">
                <h2>Courses</h2>
                <ul id="course-list" class="list-group"></ul>
                <button id="upload-video-button" class="btn btn-secondary">Upload Video</button>
                <button id="upload-resource-button" class="btn btn-secondary">Upload Resource</button>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        let courses = [];

        // Load courses from file
        fetch('courses.txt')
            .then(response => response.text())
            .then(data => {
                const courseList = data.split('\n');
                courseList.forEach(course => {
                    if (course) {
                        const [title, description] = course.split(',');
                        courses.push({ title, description });
                        const courseListItem = document.createElement('LI');
                        courseListItem.textContent = title;
                        courseListItem.classList.add('list-group-item');
                        document.getElementById('course-list').appendChild(courseListItem);
                    }
                });
            });

        // Create course form submission
        document.getElementById('create-course-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const title = document.getElementById('course-title').value;
            const description = document.getElementById('course-description').value;
            courses.push({ title, description });
            const courseListItem = document.createElement('LI');
            courseListItem.textContent = title;
            courseListItem.classList.add('list-group-item');
            document.getElementById('course-list').appendChild(courseListItem);
            // Save courses to file
            const courseData = courses.map(course => `${course.title},${course.description}`).join('\n');
            fetch('courses.txt', {
                method: 'PUT',
                body: courseData,
                headers: {
                    'Content-Type': 'text/plain'
                }
            });
            document.getElementById('course-title').value = '';
            document.getElementById('course-description').value = '';
        });

        // Upload video button click
        document.getElementById('upload-video-button').addEventListener('click', () => {
            const selectedCourseIndex = Array.prototype.indexOf.call(document.querySelectorAll('#course-list li'), document.querySelector('#course-list li:hover'));
            if (selectedCourseIndex !== -1) {
                const fileInput = document.createElement('INPUT');
                fileInput.type = 'file';
                fileInput.accept = 'video/*';
                fileInput.onchange = (e) => {
                    const selectedFile = fileInput.files[0];
                    console.log(`Uploading video: ${selectedFile.name}`);
                };
                fileInput.click();
            }
        });

        // Upload resource button click
        document.getElementById('upload-resource-button').addEventListener('click', () => {
            const selectedCourseIndex = Array.prototype.indexOf.call(document.querySelectorAll('#course-list li'), document.querySelector('#course-list li:hover'));
            if (selectedCourseIndex !== -1) {
                const fileInput = document.createElement('INPUT');
                fileInput.type = 'file';
                fileInput.accept = '*';
                fileInput.onchange = (e) => {
                    const selectedFile = fileInput.files[0];
                    console.log(`Uploading resource: ${selectedFile.name}`);
                };
                fileInput.click();
            }
        });
    </script>
</body>
</html>
