import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.data.category.DefaultCategoryDataset;

import javax.swing.*;

public class SalesBIVisualization extends JFrame {

    public SalesBIVisualization(String appTitle, String chartTitle) {
        // Create Dataset
        DefaultCategoryDataset dataset = createDataset();

        // Create Chart
        JFreeChart chart = ChartFactory.createBarChart(
                chartTitle,
                "Month",
                "Sales (in HUF)",
                dataset
        );

        // Customize Chart Panel
        ChartPanel panel = new ChartPanel(chart);
        setContentPane(panel);
    }

    private DefaultCategoryDataset createDataset() {
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();

        // Sample Data (Replace with actual DB / CSV input if needed)
        dataset.addValue(500000, "Sales", "January");
        dataset.addValue(700000, "Sales", "February");
        dataset.addValue(800000, "Sales", "March");
        dataset.addValue(600000, "Sales", "April");
        dataset.addValue(900000, "Sales", "May");

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
