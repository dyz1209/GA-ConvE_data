import csv

# 1读取cve文件
with open('../CVE_Matrix.csv', 'r') as entity1_file:
    entity1_reader = csv.reader(entity1_file)
    entity1_data = {row[0]: row[1:] for row in entity1_reader}

# 2读取cwe文件
with open('../CWE_Matrix.csv', 'r') as entity2_file:
    entity2_reader = csv.reader(entity2_file)
    entity2_data = {row[0]: row[1:] for row in entity2_reader}

# 3读取capec文件
with open('../CAPEC_Matrix.csv', 'r') as entity3_file:
    entity3_reader = csv.reader(entity3_file)
    entity3_data = {row[0]: row[1:] for row in entity3_reader}

# 4读取ioc文件
with open('../data/IOCs_Matrix.csv', 'r') as entity4_file:
    entity4_reader = csv.reader(entity4_file)
    entity4_data = {row[0]: row[1:] for row in entity4_reader}



# 处理关系文件并写入新文件
with open('../data/Characteristic_Matrix.csv', 'w', newline='') as result_file:
    result_writer = csv.writer(result_file)

    with open('../data/kg_data.csv', 'r') as relation_file:
        relation_reader = csv.reader(relation_file)

        for row in relation_reader:
            entity1_name = row[0]
            entity2_name = row[1]
            entity3_name = row[2]
            entity4_name = row[3]
            entity5_name = row[4]


            # 如果实体1和实体2都在对应的文件中存在
            if entity1_name in entity1_data and entity2_name in entity2_data and entity3_name in entity3_data and entity4_name in entity4_data:
                # 合并两个实体的特征矩阵
                # merged_row = entity1_data[entity1_name] + entity2_data[entity2_name] + entity3_data[entity3_name] + entity4_data[entity4_name]
                merged_row = [entity1_name] + entity1_data[entity1_name] + [entity2_name] + entity2_data[entity2_name] + \
                            [entity3_name] + entity3_data[entity3_name] + [entity4_name] + entity4_data[entity4_name] + [entity5_name]
                # 写入结果文件
                result_writer.writerow(merged_row)
