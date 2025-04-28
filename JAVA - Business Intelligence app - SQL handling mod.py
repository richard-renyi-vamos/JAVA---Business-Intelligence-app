import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.data.category.DefaultCategoryDataset;

import javax.swing.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class SalesBIVisualization extends JFrame {

    public SalesBIVisualization(String appTitle, String chartTitle) {
        DefaultCategoryDataset dataset = createDatasetFromSQL();

        JFreeChart chart = ChartFactory.createBarChart(
                chartTitle,
                "Month",
                "Sales (in HUF)",
                dataset
        );

        ChartPanel panel = new ChartPanel(chart);
        setContentPane(panel);
    }

    private DefaultCategoryDataset createDatasetFromSQL() {
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();

        String url = "jdbc:mysql://localhost:3306/your_database_name"; // 🖥️ Replace with your DB URL
        String user = "your_username"; // 🔐 Replace with your DB username
        String password = "your_password"; // 🔑 Replace with your DB password

        String query = "SELECT month, sales FROM sales_data"; // 📊 Your SQL query (adjust as needed!)

        try (Connection conn = DriverManager.getConnection(url, user, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            while (rs.next()) {
                String month = rs.getString("month");
                double sales = rs.getDouble("sales");
                dataset.addValue(sales, "Sales", month);
            }

        } catch (Exception e) {
            e.printStackTrace(); // 🛠️ Simple error handling (upgrade to proper logging for production!)
        }

        return dataset;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            SalesBIVisualization example = new SalesBIVisualization("Business Intelligence Dashboard", "Monthly Sales Report");
            example.setSize(800, 600);
            example.setLocationRelativeTo(null);
            example.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
            example.setVisible(true);
        });
    }
}
