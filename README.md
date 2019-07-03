# ScanIt

ScanIt is a Python application that incorporates computer vision and natural language processing techniques to scan and interpret a variety of documents. Each document type has different functions. See supported (and in-development) features below:

Business Card
- Detects Name, Job Title, Phone & Fax Number, Email Address, Address, Company Logo & Company Name
- Exports details as a VCF (Virtual Contact File) which is compatabile with Apple & other devices

Agendas
- Detects Event Name, Time & Location
- Exports as Google Calendar Event

Syllabi
- Detects Professor Name, Class Name, Location, Exam and Assignment Dates & Course Structure

* Note: ScanIt is still a work in progress. Thus, not all features have been developed and accuracy is yet to be tested. 

Dependencies
- OpenCV
- Pillow
- Regex
- Tesseract
- Numpy
