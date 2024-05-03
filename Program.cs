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
            switch (args[0])
            {
                case "clean" when args.Length >= 2:
                    if (args.Length == 2) { Data.Corpus_Clean(args[1], args[1]); }
                    else { Data.Corpus_Clean(args[1], args[2]); }
                    break;
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Mono_Decide(string[] args)
        {
            switch (args[0])
            {
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Poly_Decide(string[] args)
        {
            switch (args[0])
            {
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Trans_Decide(string[] args)
        {
            switch (args[0])
            {
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Grid_Decide(string[] args)
        {
            switch (args[0])
            {
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Matrix_Decide(string[] args)
        {
            switch (args[0])
            {
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Stream_Decide(string[] args)
        {
            switch (args[0])
            {
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Code_Decide(string[] args)
        {
            switch (args[0])
            {
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Other_Decide(string[] args)
        {
            switch (args[0])
            {
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Proto_Decide(string[] args)
        {
            switch (args[0])
            {
                default:
                    Console.WriteLine("Invalid Parameters");
                    break;

            }
        }

        static void Help_Decide(string[] args)
        {
            if (args.Length == 0)
            {
                Help.Summary();
            }
            switch (args[0])
            {
                case "all":
                    Help.All_Commands();
                    break;
                case "-d":
                case "--data":
                case "data":
                    Help.Data();
                    break;
                case "-m":
                case "--mono":
                case "mono":
                    Help.Mono();
                    break;
                case "-p":
                case "--poly":
                case "poly":
                    Help.Poly();
                    break;
                case "-t":
                case "--transpose":
                case "transpose":
                    Help.Trans();
                    break;
                case "-g":
                case "--grid":
                case "grid":
                    Help.Grid();
                    break;
                case "-M":
                case "--matrix":
                case "matrix":
                    Help.Matrix();
                    break;
                case "-s":
                case "--stream":
                case "stream":
                    Help.Streams();
                    break;
                case "-c":
                case "--code":
                case "code":
                    Help.Code();
                    break;
                case "-o":
                case "--other":
                case "other":
                    Help.Other();
                    break;
                case "-P":
                case "--proto":
                case "proto":
                    Help.Proto();
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

            string[] Pass_Params = Parameter_Pass(args);

            // First switch is for functions that don't require a parameter
            switch (args[0])
            {
                case "-h":
                case "--help":
                    Help_Decide(Pass_Params);
                    return;
                default:
                    if (Pass_Params.Length == 0)
                    {
                        Console.WriteLine("Invalid Parameters");
                        return;
                    }
                    break;
            }

            switch (args[0])
            {
                case "-d":
                case "--data":
                    Data_Decide(Pass_Params);
                    break;
                case "-m":
                case "--mono":
                    Mono_Decide(Pass_Params);
                    break;
                case "-p":
                case "--poly":
                    Poly_Decide(Pass_Params);
                    break;
                case "-t":
                case "--transpose":
                    Trans_Decide(Pass_Params);
                    break;
                case "-g":
                case "--grid":
                    Grid_Decide(Pass_Params);
                    break;
                case "-M":
                case "--matrix":
                    Matrix_Decide(Pass_Params);
                    break;
                case "-s":
                case "--stream":
                    Stream_Decide(Pass_Params);
                    break;
                case "-c":
                case "--code":
                    Code_Decide(Pass_Params);
                    break;
                case "-o":
                case "--other":
                    Other_Decide(Pass_Params);
                    break;
                case "-P":
                case "--proto":
                    Proto_Decide(Pass_Params);
                    break;
                default:
                    Console.WriteLine("cipher: option " + args[0] + ": is unknown");
                    Console.WriteLine("cipher: try 'cipher --help' for more information");
                    break;
            }
        }
    }
}
