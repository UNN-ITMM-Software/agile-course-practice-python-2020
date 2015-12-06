class LoggerError(Exception):
    pass


class TxtLogger():
    def __init__(self, path_to_log):
        print('path_to_log', path_to_log)






#
#         package ru.unn.agile.ComplexNumber.infrastructure_lab3_legacy;
#
# import ru.unn.agile.ComplexNumber.viewmodel_lab3_legacy.ILogger;
#
# import java.io.BufferedReader;
# import java.io.BufferedWriter;
# import java.io.FileReader;
# import java.io.FileWriter;
# import java.text.SimpleDateFormat;
# import java.util.ArrayList;
# import java.util.Calendar;
# import java.util.List;
# import java.util.Locale;
#
# public class TxtLogger implements ILogger {
#     private static final String DATE_FORMAT_NOW = "yyyy-MM-dd HH:mm:ss";
#     private final BufferedWriter writer;
#     private final String filename;
#
#     private static String now() {
#         Calendar cal = Calendar.getInstance();
#         SimpleDateFormat sdf = new SimpleDateFormat(DATE_FORMAT_NOW, Locale.ENGLISH);
#         return sdf.format(cal.getTime());
#     }
#
#     public TxtLogger(final String filename) {
#         this.filename = filename;
#
#         BufferedWriter logWriter = null;
#         try {
#             logWriter = new BufferedWriter(new FileWriter(filename));
#         } catch (Exception e) {
#             e.printStackTrace();
#         }
#         writer = logWriter;
#     }
#
#     @Override
#     public void log(final String s) {
#         try {
#             writer.write(now() + " > " + s);
#             writer.newLine();
#             writer.flush();
#         } catch (Exception e) {
#             System.out.println(e.getMessage());
#         }
#     }
#
#     @Override
#     public List<String> getLog() {
#         BufferedReader reader;
#         ArrayList<String> log = new ArrayList<String>();
#         try {
#             reader = new BufferedReader(new FileReader(filename));
#             String line = reader.readLine();
#
#             while (line != null) {
#                 log.add(line);
#                 line = reader.readLine();
#             }
#         } catch (Exception e) {
#             System.out.println(e.getMessage());
#         }
#
#         return log;
#     }
#
# }
