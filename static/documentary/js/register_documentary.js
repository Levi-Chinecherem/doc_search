$(document).ready(function () {
    // Function to update and show the modal with a message
    function showModal(message, isSuccess) {
        const resultModal = $('#resultModal'); // Moved inside the function for better scoping
        const resultMessage = $('#resultMessage');
        resultMessage.text(message);

        if (isSuccess) {
            resultMessage.removeClass('text-danger').addClass('text-success');
        } else {
            resultMessage.removeClass('text-success').addClass('text-danger');
        }

        resultModal.modal('show');
    }

    // Show the modal when the page loads if the modal has a message
    const resultMessage = $('#resultMessage');
    if (resultMessage.text().trim() !== '') {
        showModal(resultMessage.text(), true); // Automatically show modal on page load
    }

    // Example: Trigger the modal when a new documentary is added
    // You can call this function based on your specific use case
    // For example, in your form submission AJAX callback.
    // showModal('Documentary added successfully', true);
});
