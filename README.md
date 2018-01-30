<h2>FaceRecognition-tool</h2>
<p>A simple, modular face recognition tool, can be used for demo or can be embedded inside applications.</p>
<p>Built using OpenFace. </p>

<h3>How to run?</h3>
<p>Install all dependencies, installation instructions can be found <a href = "https://github.com/ageitgey/face_recognition">here</a>
<p>Steps:</p>
<p>1. change NAME variable in FaceGenerator.py to your name</p>
<p>2. Run FaceGenerator.py until you are satisfied with your pose, make sure facial features are clearly visible. </p>
<p>3. Press 'q' to stop, now the application will automatically generate the NAME.npy file for the image.
<p>4. Now run RealTime.py, the app will automatically recognize image. </p>
<p>You can also copy the image directly into KnownFaces directory, the name of file should be the name to be displayed if face is recognised.
Make sure you generate encodings for newly placed image by calling, encode_single() of Encodings.py module.</p>

<h3>How to integrate with other apps? </h3>
<p>The major component of face recognition system is generation of encoding for each face, this app has functions to produce and retrive
 encodings, <strong>Encoding.py</strong> module contains 3 classes : </p>
 <p>1. <strong>Encode(Thread):</strong> Base class which generates an encoding file for given image file. This class extends Thread class, 
 so this class should be executed as a thread always, by calling start() method on the class.</p>
 <p>2. <strong>InitlaizeEncodingsOfKnownFaces:</strong> Base class which can be used to obtain all currently previously available encoding files.</p>
 <p> Parameters : encoding_directory : Specifies the diectory which contains encoding files </p>
 <p> getEncodings() : This function returns an array of structure : [{name : encoding},..] where name represents the label and
 encoding is a numpy array representing encoded data. </p>
 
 <p><strong>Functions: </p>
 <p> encode_all_faces() : Generates a pool of threads, where each thread is an instance of Encode(Thread) object , this function can be
 called to generate encoding files of all known images.</p>
 <p><strong>encode_single(filename):<strong> Generate encoding for a single image file, specifiy image file as parameter</p>
 
 <h3>Result: </h3>
 <p>1. </p>
 <img src = "./SampleOutput/Prasanna.jpg"/>
 
 <p>2. </p>
 <img src = "./SampleOutput/Galye.jpg"/>
 
 <p>3. </p>
 <img src = "./SampleOutput/Obama.jpg"/>
 
 <p>4. </p>
 <img src = "./SampleOutput/Trump.jpg"/>
 
 <p>6. </p>
 <img src = "./SampleOutput/NoFace.jpg"/>
 
 
 
 
