using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Win32;
using System.Runtime.InteropServices;
using System.Threading;

namespace Test
{
    public partial class Main : Form
    {
        public Main(String Str_Value="")
        {
            InitializeComponent();
            textBox1.Text = Str_Value;
        }
        public string Str_value { get; set; }
   
        private void Main_Load(object sender, EventArgs e)
        {
           
        }

        private void Label1_Click(object sender, EventArgs e)
        {

        }

        private void Button2_Click(object sender, EventArgs e)
        {
            new_device ss = new new_device();
            ss.Show();
            this.Close();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Button3_Click(object sender, EventArgs e)
        {
            login ss = new login();
            ss.Show();
            this.Close();
        }
        // start on start up
        private void CheckBox1_CheckedChanged(object sender, EventArgs e)
        {
            RegistryKey rk = Registry.CurrentUser.OpenSubKey
            ("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", true);

            if (chkStartUp.Checked)
                rk.SetValue("SmartPcGuard", Application.ExecutablePath);
            else
                rk.DeleteValue("SmartPcGuard", false);

            if (checkBox2.Checked == true)
            { chkStartUp.Checked = false; }
        }

        // disable start up


        private void ListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }


        private void formVisibleChanged(object sender, EventArgs e)
        {
           

        }

        private void CheckedListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Button4_Click(object sender, EventArgs e)
        {
            new_device_bluetooth ss = new new_device_bluetooth();
            ss.Show();
            this.Close();
        }

        private void CheckBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox2.Checked)
            {
                Microsoft.Win32.RegistryKey key = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", true);
                key.DeleteValue("SmartPcGuard", false);
            }
            if (chkStartUp.Checked == true)
            { checkBox2.Checked = false;}
        }

        private void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
