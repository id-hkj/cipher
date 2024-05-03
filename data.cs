namespace Cipher
{
    public class Data
    {
        public static void Corpus_Clean(string read_file, string out_file)
        {
            read_file = Path.GetFullPath(read_file);
            out_file = Path.GetFullPath(out_file);

            if (!File.Exists(read_file)) {
                Console.WriteLine("ERROR: Invalid read file");
                return;
            }

            StreamReader sr = new(read_file);
            string total = sr.ReadToEnd();
            string final = "";
            
            Console.WriteLine("Opened file");
            Console.WriteLine("Starting clean...");
            
            foreach (char character in total)
            {
                switch (Convert.ToInt32(character))
                {
                    case 32:
                    case 10:
                        final += " ";
                        break;
                    case int c when (c >= 65 & c <= 90):
                        final += character;
                        break;
                    case int c when (c >= 97 & c < 122):
                        final += Convert.ToChar(Convert.ToInt32(character) - 32);
                        break;
                }
            }
            Console.WriteLine(final);

            Console.WriteLine("Clean finished.");
            Console.WriteLine("Writing result to file");

            using (StreamWriter sw = new(out_file))
            {
                sw.WriteLine(final);
            }
            Console.WriteLine("Complete.");
        }
    }
}
