using System;
using System.ComponentModel.Design;
using System.IO;

namespace Cipher
{
    class Program
    {
        static string[] Parameter_Pass(string[] els)
        {
            var new_arr = new string[els.Length - 1];
            for (int i = 0; i < new_arr.Length; i++)
            {
                new_arr[i] = els[i + 1];
            }
            return new_arr;
        }

        static void Data_Decide(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Invalid Parameters");
                return;
            }
            switch (args[0])
            {
                case "clean" when args.Length >= 2:
                    if (args.Length == 2) { Data.corpus_clean(args[1], args[1]); }
                    else { Data.corpus_clean(args[1], args[2]); }
                    break;
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Invalid Parameters");
                return;
            }

            switch (args[0])
            {
                case "-h":
                case "--help":
                    Console.WriteLine("TUsage: cipher [options...]");
                    Console.WriteLine("data - Some Corpus and Fittness functions");
                    Console.WriteLine("mono - Monalphabetic substitution cipher solver/encoders");
                    Console.WriteLine("poly - Polyalphabetic substitution cipher solver/encoders");
                    Console.WriteLine("transpose - Transposition cipher solver/encoders");
                    Console.WriteLine("grid - solver/encoder for ciphers based on grids");
                    Console.WriteLine("matrix - solver/encoder for ciphers based on matrices");
                    Console.WriteLine("stream - Stream ciphers solver/encoder");
                    Console.WriteLine("code");
                    Console.WriteLine("proto - Protomechanical ciphers solver/encoder");
                    Console.WriteLine("other - Miscelanious ciphers");
                    Console.WriteLine();
                    Console.WriteLine("This is not the full help, this menu is stripped into categories.");
                    Console.WriteLine("Use " + '"' + "--help category + '"' + " to get an overview of all categories.");
                    Console.WriteLine("For all options use the manual or " + '"' " "--help all" + '"' + ". (not yet implemented)");
                    Console.WriteLine();
                    Console.WriteLine("As of writing, only data has been implemented.");
                    break;
                case "data":
                    Data_Decide(Parameter_Pass(args));
                    break;
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;
            }
        }
    }
}
