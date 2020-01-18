using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using Microsoft.Win32;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.IO;
using System.Threading;
using InTheHand.Net.Sockets;


namespace Test
{
    public partial class login : Form
    {
        [StructLayout(LayoutKind.Sequential)]
        private struct KBDLLHOOKSTRUCT
        {
            public Keys key;
            public int scanCode;
            public int flags;
            public int time;
            public IntPtr extra;
        }
        //System level functions to be used for hook and unhook keyboard input  
        private delegate IntPtr LowLevelKeyboardProc(int nCode, IntPtr wParam, IntPtr lParam);
        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr SetWindowsHookEx(int id, LowLevelKeyboardProc callback, IntPtr hMod, uint dwThreadId);
        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern bool UnhookWindowsHookEx(IntPtr hook);
        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr CallNextHookEx(IntPtr hook, int nCode, IntPtr wp, IntPtr lp);
        [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr GetModuleHandle(string name);
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        private static extern short GetAsyncKeyState(Keys key);
        //Declaring Global objects     
        private IntPtr ptrHook;
        private LowLevelKeyboardProc objKeyboardProcess;

        private IntPtr captureKey(int nCode, IntPtr wp, IntPtr lp)
        {
            if (nCode >= 0)
            {
                KBDLLHOOKSTRUCT objKeyInfo = (KBDLLHOOKSTRUCT)Marshal.PtrToStructure(lp, typeof(KBDLLHOOKSTRUCT));

                // Disabling Windows keys 

                if (objKeyInfo.key == Keys.RWin || objKeyInfo.key == Keys.LWin || objKeyInfo.key == Keys.Tab && HasAltModifier(objKeyInfo.flags) || objKeyInfo.key == Keys.Escape && (ModifierKeys & Keys.Control) == Keys.Control)
                {
                    return (IntPtr)1; // if 0 is returned then All the above keys will be enabled
                }
            }
            return CallNextHookEx(ptrHook, nCode, wp, lp);
        }

        bool HasAltModifier(int flags)
        {
            return (flags & 0x20) == 0x20;
        }

        /* Code to Disable WinKey, Alt+Tab, Ctrl+Esc Ends Here */
        [DllImport("user32")]

        public static extern bool ExitWindowsEx(GraphicsUnit uFlags, uint dwReason);
        public login()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Locking_Test();
            

        }
        
        private void Locking_Test()
        {
            string myString = "";
            foreach (System.IO.DriveInfo drive in System.IO.DriveInfo.GetDrives())
            {
                if ((drive.DriveType == System.IO.DriveType.Removable))
                {
                   
                    string resumeFile = drive.Name + @"locker\locker.txt";

                    if (File.Exists(resumeFile))
                    {
                        System.IO.StreamReader myFile = new System.IO.StreamReader(resumeFile);
                        myString = myString + " " + myFile.ReadToEnd();
                        myFile.Close();

                    }
                }
            }


            if (myString.Contains("abc"))
            {

                this.Hide();
                bool Isopen = false;
                foreach (Form f in Application.OpenForms)
                {
                    if (f.Text== "Main")
                    {
                        Isopen = true;
                        break;
                    }
                }

                if (Isopen == false)
                {
                    Main ss = new Main();
                    ss.Show();
                }
            }


        
            else
            {
                
            }

        }

        private void Label2_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.TopMost = true;
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            ProcessModule objCurrentModule = Process.GetCurrentProcess().MainModule;
            objKeyboardProcess = new LowLevelKeyboardProc(captureKey);
            ptrHook = SetWindowsHookEx(13, objKeyboardProcess, GetModuleHandle(objCurrentModule.ModuleName), 0);
        }

        private void Panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void Button2_Click(object sender, EventArgs e)
        {
            this.Close();

        }
        public string pwd = "0";
        private void Button1_Click(object sender, EventArgs e)
        {
            if (textBox2.Text ==  "")
            {
                MessageBox.Show("Please enter Password");
            }
            else if (textBox2.Text == pwd)
            {
                this.Hide();
                Main ss = new Main();
                ss.Show();
            }
            else
            {
                MessageBox.Show("Wrong Password");
            }
        }
      /*  {
            SqlConnection con = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\downloads\Test(2)\Test\test.mdf;Integrated Security=True;Connect Timeout=30");
            SqlDataAdapter sqa = new SqlDataAdapter("Select count(*) From password where password ='" + textBox2.Text, con);
            DataTable dt = new DataTable();
            sqa.Fill(dt);

            if (dt.Rows[0][0].ToString() == "1")
            {
                this.Hide();
                Main ss = new Main();
                ss.Show();
            }
            else
            {
                MessageBox.Show("Wrong Password");
            }
        } */

       

        private void Label3_Click(object sender, EventArgs e)
        {

        }

        private void PictureBox1_Click(object sender, EventArgs e)
        {

        }
        
        
        
        // disable task manager
        public static void ToggleTaskManager(string keyValue)
        {
            RegistryKey objRegistryKey = Registry.CurrentUser.CreateSubKey("Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System");
            objRegistryKey.SetValue("DisableTaskMgr", keyValue);
            objRegistryKey.Close();
        }

        private void Button3_Click(object sender, EventArgs e)
        {
            Process.Start("shutdown.exe", "-s -t 00");
        }

        private void Button4_Click(object sender, EventArgs e)
        {
            ExitWindowsEx(0, 0);
        }

        private void Button5_Click(object sender, EventArgs e)
        {
            Process.Start("shutdown.exe", "-r -t 00");
        }
        // disabling Alt+f4
        protected override bool ProcessCmdKey(ref System.Windows.Forms.Message msg, System.Windows.Forms.Keys keydata)
        {
            if (keydata == (Keys.Alt | Keys.F4))
            {
                MessageBox.Show("Alt+F4 is Disabled", "SmartGuard.exe");
                return true;
            }
            else
            {
                return base.ProcessCmdKey(ref msg, keydata);
            }
        }

            private void Button3_Click_1(object sender, EventArgs e)
        {
            this.Hide();

            Main ss = new Main();
            ss.Show();
        }

        private void Label5_Click(object sender, EventArgs e)
        {

        }

        private void TextBox2_TextChanged(object sender, EventArgs e)
        {

        }

        public string BTdevice = "V30+";
        private void Button6_Click(object sender, EventArgs e)
        {
            BluetoothDeviceInfo[] devices;
            using (BluetoothClient sdp = new BluetoothClient())
                devices = sdp.DiscoverDevices();


            foreach (BluetoothDeviceInfo deviceInfo in devices)
            {
                if (deviceInfo.DeviceName == BTdevice)
                {

                    this.Hide();
                    Main ss = new Main();
                    ss.Show();
                }
                else
                {
                    MessageBox.Show("No saved devices detected");
                }
            }
        }

        private void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }
        
        
    }
}
