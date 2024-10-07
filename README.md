# GA-ConvE_data
The datasets and data processing used in the GA-ConvE paper include the following components:

（1）CVE, CWE, CAPEC Descriptions: The dataset is constructed from the relationships between APT (Advanced Persistent Threat), CVE (Common Vulnerabilities and Exposures), and IOCs (Indicators of Compromise) extracted from APT reports, as well as the relationships between CVE, CWE (Common Weakness Enumeration), and CAPEC (Common Attack Pattern Enumeration and Classification) collected from the official MITRE website, which are compiled into kg_data.csv.

（2）IOCs Data: The IOCs data comes from various professional institutions and has been verified by industry experts, ensuring a high degree of professionalism. Due to confidentiality concerns, only a portion of the IOC data is shown here.

(3)CVE, CWE, CAPEC Data: The files **cve_data.csv**, **cwe_data.cs**v, and **capec_data.csv** contain the respective descriptions of these datasets, which were obtained from MITRE.

(4)Knowledge Graph Data: **kg_data.csv** was created based on the relationships between various entities, forming the links between entities that serve as the foundation for constructing the knowledge graph. It also includes non-attack data, where certain entities in the data are left blank.

(5)Entity Feature Extraction Scripts:**CVE_Extract.py** is used to extract the CVE entity feature matrix, **CVE_Matrix.csv**.**CWE_Extract.py** is used to extract the CWE entity feature matrix, **CWE_Matrix.csv**.**CAPEC_Extract.py** is used to extract the CAPEC entity feature matrix, **CAPEC_Matrix.csv**.**IOCs_Extract.py** is used to extract the IOC entity feature matrix, **IOCs_Matrix.csv**.

(6)Matrix Concatenation: **Matrix_Concatenation.py** is used to concatenate the feature matrices of various entities based on the links in **kg_data.csv**, resulting in the final feature matrix, **Characteristic_Matrix.csv**.

(7)Relationship Matrix Extraction: **RelationMatrix_Extract.p** extracts the relationships between different data points, ultimately generating the relationship matrix **Relation_Matrix.csv**.

(8)Triplet Extraction: **Triplets_Extract.py** is used to extract the triplets into **Triplets.txt**.

(9)Main Script: **main.py** is the main script that calls other functions.



Below is our data processing workflow:

1、Run the **main.py script**.

2、In the console, input **CVE_Extract** to call **CVE_Extract.py** and generate the **CVE_Matrix.csv** file.

3、In the console, input **CWE_Extract** to call **CWE_Extract.py** and generate the **CWE_Matrix.csv** file.

4、In the console, input **CAPEC_Extract** to call **CAPEC_Extract.py** and generate the **CAPEC_Matrix.csv** file.

5、In the console, input **IOCs_Extract** to call **IOCs_Extract.py** and generate the **IOCs_Matrix.csv** file.

6、In the console, input **Matrix_Concatenation** to call **Matrix_Concatenation.py** and generate the **Characteristic_Matrix.csv** file.

7、In the console, input **RelationMatrix_Extract** to call **RelationMatrix_Extract.py** and generate the **Relation_Matrix.csv** file.

8、In the console, input **Triplets_Extract** to call **Triplets_Extract.py** and generate the **Triplets.txt** file.

9、In the console, input **0** to exit the program.

Notes:

1、The final processed data used for the experiment includes the **Characteristic_Matrix.csv** feature matrix and the **Relation_Matrix.csv** relationship matrix, which are used for classification experiments. The generated triplets in **Triplets.txt** are used for further inference experiments.

2、The data in the **GA-ConvE** folder contains the processed data and code that has already been handled according to the workflow described above. The data in the **GA-ConvE_empty** folder contains the unprocessed data and code.






















