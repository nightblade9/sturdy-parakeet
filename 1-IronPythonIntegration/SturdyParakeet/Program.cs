using System;
using System.IO;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

namespace SturdyParakeet
{
    class Program
    {
        private static string ScriptFileName = "hello_you.py";

        static void Main(string[] args)
        {
            Console.WriteLine($"Hello World! Running {ScriptFileName} ...");

            var engine = Python.CreateEngine();
            var scope = engine.CreateScope();
            engine.ExecuteFile("hello_you.py", scope);

            dynamic func = scope.GetVariable("new_guid");
            var result = func();
            Console.WriteLine($"wut: r={result}");
        }
    }
}
