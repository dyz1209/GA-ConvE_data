# GA-ConvE_data
The dataset used in the GA-ConvE paper consists of the following components:

（1）The CVE, CWE, and CAPEC descriptions, along with the relationships between APT (extracted from APT reports), CVE, and IOCs, as well as the relationships between CVE, CWE, and CAPEC (collected from the official MITRE website), were used to construct the kg_data.csv.

（2）The IOCs data we used is sourced from various professional organizations, and all of the data has been validated by industry experts, ensuring a high level of professionalism. Due to confidentiality reasons, we only display partial information from a subset of the IOCs data here.

Below is our data processing workflow:

（1）We run the scripts CVE_Extract.py, CWE_Extract.py, and CAPEC_Extract.py to generate CVE_Matrix.csv, CWE_Matrix.csv, and CAPEC_Matrix.csv, respectively. These files serve as the feature matrices corresponding to each entity.

（2）We then run the Matrix_Concatenation.py script, which concatenates the feature matrices of various entities, ultimately producing the final feature matrix, Characteristic_Matrix.csv. During this concatenation process, the names of the entities are retained for later classification and filtering.

（3）The RelationMatrix_Extract.py script is executed to extract the relationship matrix, producing the Relation_Matrix.csv file. Additionally, we run Triplets_Extract.py to extract triplets of attack data, which are stored in Triplets.txt. The triplet extraction for unclassified data is shown here, and in practice, the data in kg_data.csv is classified according to the final classification result before triplets are extracted.

The final processed data includes the Characteristic_Matrix.csv feature matrix and the Relation_Matrix.csv feature matrix, which are used for classification experiments. The generated triplets file, Triplets.txt, is used for further inference experiments.

Notes:

（1）cve_data.csv, cwe_data.csv, and capec_data.csv contain the descriptions of the corresponding data obtained from MITRE.

（2）kg_data.csv contains the links between entities, based on the relationships between them, which serve as the foundation for building the knowledge graph. It also includes non-attack data, where one of the entities in the dataset may be set as null.

（3）CVE_Extract.py is the code used to extract the CVE entity feature matrix, CWE_Extract.py is used for extracting the CWE entity feature matrix, and CAPEC_Extract.py extracts the CAPEC entity feature matrix. IOCs_Matrix.csv is the pre-extracted feature matrix for IOCs entities, and due to confidentiality concerns, the detailed process is not disclosed.

（4）Matrix_Concatenation.py is responsible for concatenating the feature matrices extracted from each entity based on the links in Kg_data.csv, resulting in the final feature matrix.

（5）RelationMatrix_Extract.py extracts the relationships between data points, ultimately producing the relationship matrix.

（6）Triplets_Extract.py is used to extract triplets from the data.

（7）The data in the GA-ConvE (1) file is the processed data and code, following the steps described above. The data in the GA-ConvE (2) file is unprocessed and contains the raw data and code.
