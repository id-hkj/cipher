using System;

namespace Cipher
{
    public class Help
    {
        public static void Summary()
        {
            Console.WriteLine("Usage: cipher  [options...]");
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
            Console.WriteLine("Use \"--help category\" to get an overview of all categories.");
            Console.WriteLine("For all options use the manual or \"--help all\".");
            Console.WriteLine();
            Console.WriteLine("As of writing, only data has been implemented.");
        }

        public static void All_Commands()
        {
            Console.WriteLine();
        }

        public static void Data()
        {
            Console.WriteLine();
        }

        public static void Mono()
        {
            Console.WriteLine();
        }

        public static void Poly()
        {
            Console.WriteLine();
        }

        public static void Trans()
        {
            Console.WriteLine();
        }

        public static void Grid()
        {
            Console.WriteLine();
        }

        public static void Matrix()
        {
            Console.WriteLine();
        }

        public static void Streams()
        {
            Console.WriteLine();
        }

        public static void Code()
        {
            Console.WriteLine();
        }

        public static void Other()
        {
            Console.WriteLine();
        }

        public static void Proto()
        {
            Console.WriteLine();
        }
    }
}
