import org.apache.spark.sql.{SparkSession, functions => F}
import org.apache.spark.sql.functions.udf

object UDFRegistrationExample extends App {
 // Create a Spark session
 val spark = SparkSession.builder()
   .appName("UDF Registration Example")
   .master("local[*]")
   .getOrCreate()

 // Define the UDF function
 val stringLengthUDF = udf((s: String) => if (s == null) 0 else s.length)

 // Register the UDF with Spark SQL
 spark.udf.register("stringLength", stringLengthUDF)

 // Create a DataFrame
 import spark.implicits._

 val df = Seq("apple", "banana", "cherry").toDF("fruit")

 // Register the DataFrame as a temporary view
 df.createOrReplaceTempView("fruits")

 // Use the UDF in a SQL query
 val resultDF = spark.sql("SELECT fruit, stringLength(fruit) AS length FROM fruits")

 // Show the result
 resultDF.show()

 // Stop the Spark session
 spark.stop()
}
