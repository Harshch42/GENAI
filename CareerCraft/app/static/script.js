function updateInputVisibility(selectId, fileId, urlId, textId) {
    const select = document.getElementById(selectId);
    const fileInput = document.getElementById(fileId);
    const urlInput = document.getElementById(urlId);
    const textInput = document.getElementById(textId);

    fileInput.classList.add('hidden');
    urlInput.classList.add('hidden');
    textInput.classList.add('hidden');

    switch (select.value) {
        case 'file':
            fileInput.classList.remove('hidden');
            break;
        case 'url':
            urlInput.classList.remove('hidden');
            break;
        case 'text':
            textInput.classList.remove('hidden');
            break;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const jdType = document.getElementById('jd_type');
    const resumeType = document.getElementById('resume_type');

    jdType.addEventListener('change', () => updateInputVisibility('jd_type', 'jd_file_input', 'jd_url_input', 'jd_text_input'));
    resumeType.addEventListener('change', () => updateInputVisibility('resume_type', 'resume_file_input', 'resume_url_input', 'resume_text_input'));

    // Initialize visibility
    updateInputVisibility('jd_type', 'jd_file_input', 'jd_url_input', 'jd_text_input');
    updateInputVisibility('resume_type', 'resume_file_input', 'resume_url_input', 'resume_text_input');
});