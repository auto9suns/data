
class postgres():

    def __init__(self):
        self.connectdb()

    def connectdb(self):
        pass

    @staticmethod
    def make_table_create(column_type, table_name):
        create_table_clause = "create " + table_name + " "
        table_type= "("
        for i in range(len(column_type)):
            pair = column_type[i]
            if i == len(column_type)-1:
                table_type = table_type + pair.get("column") + " " + pair.get("type") + ")"
            else:
                table_type = table_type + pair.get("column") + " " + pair.get("type") + ","
        return create_table_clause + table_type



if __name__ == "__main__":
   print (postgres.make_table_create([{"column":"A", "type": "varchar(64)"},{"column": "B", "type":"integer"}],"test"))




